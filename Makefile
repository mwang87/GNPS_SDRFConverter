run:
	nextflow run --resume convert_sdrf.nf

test_redu:
	python ./bin/convert_redu.py "MSV000078556" redu_MSV000078556.sdrf.tsv
	parse_sdrf validate-sdrf --sdrf_file redu_MSV000078556.sdrf.tsv

#validate_sdrf:
	