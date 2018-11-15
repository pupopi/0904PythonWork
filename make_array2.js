/* 1から30の整数の中で、
   3か5か7か11で割り切れる数字のみが格納された配列を作成してください。 */

const make_array = (x) => {
    const range = Array.from({length: x}, (_, i) => i+1);
    const range_numbers = range.map(function(value){
        return value+1
    });
    function beDisible(value) {
        return (value%3==0 || value%5==0 || value%7==0 || value%11==0 )
    };
    const array = range_numbers.filter(beDisible);
    console.log(array);
};

make_array(30);