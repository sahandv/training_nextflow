#!/bin/env nextflow 

// Define the processes
process corr_calc {
    publishDir params.outDir

    input:
    path code
    file data_1
    file data_2
    
    output:
    path 'corr_data/'

    label 'low_mem'
    
    shell:
    '''
    python scripts/corr.py  -i . -o corr_data
    '''
}
