import vcf
import yaml
from interStruct import Variant, Sample

class vcfConverter:

    def __init__(self, vcf_file):

        vcf_reader = vcf.Reader(open(vcf_file, 'r'))

        self.samples = {}
        for sample in vcf_reader.samples:
            print(sample)
            self.samples[sample] = Sample(name = sample)

        self.variants = []
        for record in vcf_reader:
            variant = Variant(record.CHROM, 
                              record.POS, 
                              record.ID, 
                              record.REF, 
                              record.ALT, 
                              record.QUAL, 
                              record.FILTER, 
                              record.INFO)
            for call in record.samples:
                variant.CALLS.append({'NAME':call.sample, 'DATA':call.data._asdict()})
            self.variants.append(variant)    


    def convertVariants(self, def_file):
        with open(def_file, 'r') as fi:
            definition = yaml.load(fi, Loader=yaml.FullLoader)

        struct = []
        for variant in self.variants:
            struct.extend(variant.toSchema(definition))

        return struct


