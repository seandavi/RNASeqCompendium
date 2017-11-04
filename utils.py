import subprocess
import argparse
import glob
import os

def fastq_dump(srr, gzip = True, outdir = '.', extra_args = ""):
    cmd = "fastq-dump -X 10000"
    if(gzip):
        cmd += " --gzip"
    cmd += ' --outdir {} '.format(outdir)
    cmd += extra_args
    cmd += " " + srr
    subprocess.run(cmd, shell = True, check = True)
    fname_match = srr + "*.fastq"
    if(gzip):
        fname_match += '.gz'
    return(sorted(glob.glob(os.path.join(outdir,fname_match))))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('srr')
    args = parser.parse_args()
    fastq_dump(args.srr)
    
