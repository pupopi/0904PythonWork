/* 自然数 n を任意の数格納した配列 ns と、 自然数 x を引数として、 ns から x 回、
   逐次的にその時点での最大の n を 1 減らした配列にするメソッド cherry_pick を作成してください。 
   
   cherry_pick([9, 7, 8], 3) # => [ 7, 7, 7 ]
   cherry_pick([9, 7, 8], 10) # => [ 4, 5, 5 ]                                              */


const cherry_pick = (ns, x) => {
    if( x>0 ) {
        let max_ns = ns.indexOf(Math.max.apply(null,ns));
        ns.splice(max_ns,1,ns[max_ns]-1);
        return cherry_pick(ns, x-1);
    } else {
        console.log(ns);
    } 
};

cherry_pick([9, 7, 8], 3)       // → [7, 7, 7]
cherry_pick([9, 7, 8], 10)      // → [4, 5, 5]