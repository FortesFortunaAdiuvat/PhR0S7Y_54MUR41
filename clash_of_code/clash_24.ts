const n: number = parseInt(readline());
let d = {'guitar': 'plinx','drums':'tss'};
for (let i = 0; i < n; i++) {
    let ins = readline();
    if(ins == 'guitar'){
        if(d[ins]=='plinx'){
            console.log(d[ins]);
            d[ins]='plonx';
        }else{
            console.log(d[ins]);
            d[ins]='plinx';
        }
    }else if(ins == 'drums' && i == n-1){
        console.log('tss');
    }else{
        console.log('badum');
    }
}