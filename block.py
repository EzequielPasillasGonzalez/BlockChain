import json
import os
import hashlib

BLOCKCHAIN_DIR = 'blockchain/'

def get_hash(prevBlock):
    with open(BLOCKCHAIN_DIR + prevBlock, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()

def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    
    results = []
    
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
            
        prev_hash = block['prevBlock']['hash']
        prev_filename = block['prevBlock']['filename']
        
        actual_hash = get_hash(prev_filename)
        
        if prev_hash == actual_hash:
            res = 'Ok'
        else:
            res = 'Fue cambiado'
            
        
        results.append({'block': prev_filename, 'result': res})
            
        
    return results
    

def write_block(vendedor, comprador, montoCompra):
    
    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    
    data = {
        "vendedor": vendedor,    
        "comprador": comprador,
        "montoCompra": montoCompra,
        "prevBlock": {
            "hash": get_hash(prev_block),
            "filename": prev_block
        }
    }
    
    blockAcutal = BLOCKCHAIN_DIR + str(blocks_count + 1)
    
    with open(blockAcutal, 'w') as  f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')
        
        
def main():
    # write_block(vendedor="Alex", comprador='Kate', montoCompra=100)
    check_integrity()

if __name__ == '__main__':
    main()