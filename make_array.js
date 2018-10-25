/* 1から30の整数の中で、
   3か5か7か11で割り切れる数字のみが格納された配列を作成してください。 */


function makeArray() {
    array = [];
    for(i=1; i<=30; i++) {
        if( i%3==0 | i%5==0 | i%7==0 | i%11==0 ) continue;
        array.push(i);
    }
    console.log(array);
}

makeArray()