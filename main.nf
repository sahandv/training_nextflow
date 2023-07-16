#!/usr/local/bin/nextflow 

nextflow.enable.dsl=2

include { corr_calc } from './modules/corr'
include { gen_data_1 } from './modules/gen'
include { gen_data_2 } from './modules/gen'


log.info """\
=======================================================================================
Corss Skilling Demo
=======================================================================================
Created by the Sydney Informatics Hub, The University of Sydney
Cite this pipeline @ N/A
=======================================================================================
Workflow run parameters 
=======================================================================================
input       : ${params.input}
outDir      : ${params.outDir}
workDir     : ${workflow.workDir}
Profile description : ${params.config_profile_description}
=======================================================================================
Execuation start time: ${new Date()}
=======================================================================================
"""
def helpMessage() {
    log.info"""
  Usage:  nextflow run main.nf --configs_file <configs_file.yaml> --modules_file <modules_file.yaml>
  Arguments:
    --name_1: name of the first file
    --name_2: name of the second file
    --code: path to the code to run the pipeline 
    --outDir: output directory
	
""".stripIndent()
}

code_channel = Channel.fromPath(params.code)

workflow {
    if ( params.help || !params.name_1 || !params.name_2 || !params.outDir ){
        // Invoke the help function above and exit
              helpMessage()
              exit 1
    }
    else{
        data_1 =  gen_data_1(code_channel,params.name_1)
        data_2 =  gen_data_2(code_channel,params.name_2)
        corr =  corr_calc(code_channel,data_1, data_2)
    }
}