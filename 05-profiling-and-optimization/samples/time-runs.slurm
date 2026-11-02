#!/bin/bash
#SBATCH --job-name=qhpc-time-runs
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:05:00
#SBATCH --mem=1G
#SBATCH --output=time-runs-%j.out

# Times the same program three times on one compute node.
# Usage: sbatch time-runs.slurm ./hotspot-O0

program=${1:?give the program to time, for example ./hotspot-O0}

echo "Node: $(hostname)"
echo "Program: $program"

for run in 1 2 3; do
  echo
  echo "--- Run $run ---"
  time "$program"
done
