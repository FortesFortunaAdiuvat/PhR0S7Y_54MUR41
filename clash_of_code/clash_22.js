/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

 const count = parseInt(readline());
 var inputs = readline().split(' ');
 var vec = []
 for (let i = 0; i < count; i++) {
     const unary = inputs[i];
     vec.push(unary.length)
 }
 
 // Write an answer using console.log()
 // To debug: console.error('Debug messages...');
 
 
 
 console.log('1'.repeat(vec.reduce((c,p) => c+p, 0)));