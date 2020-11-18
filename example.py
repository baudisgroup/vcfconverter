from vcfConverter import vcfConverter

converter = vcfConverter(vcf_file = 'HG00096.cnv.vcf')
beacon_struct = converter.convertVariants(def_file = 'definition.yaml')

for s in beacon_struct:
    print(s)