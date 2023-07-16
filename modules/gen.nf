#!/bin/env nextflow 

// Define the processes
process gen_data_1 {
    input:
    path code
    val name
    
    output:
    file 'data/1.csv'

    label 'low_mem'
    
    shell:
    '''
    python scripts/gen.py -d data -n 500 -c "!{name}" -f 1.csv
    '''
}

process gen_data_2 {
    input:
    path code
    val name
    
    output:
    file 'data/2.csv'

    label 'low_mem'
    
    shell:
    '''
    python scripts/gen.py -d data -n 500 -c "!{name}" -f 2.csv
    '''
}

