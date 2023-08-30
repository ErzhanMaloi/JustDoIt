// // // // // // // let family;
// // // // // // // let admin;
// // // // // // // family = "josh";
// // // // // // // admin = family;
// // // // // // result = prompt("vary good", []);
// // // // // let counter = 1;
// // // // // let a = counter++; // (*) меняем ++counter на counter++
// // // // // a = counter;
// // // // // alert(a); // 1
// // // // // let a = prompt("Первое число?", 1);
// // // // // let b = prompt("Второе число?", 2);

// // // // // alert(+a + +b); // 12

// // // // // let age = prompt("vvedi");
// // // // // let aga;
// // // // // aga = age;
// // // // // aga = (aga >= 14 && aga<=90) ? alert(aga) : alert("vvedeno neverno");
// // // // // let age = prompt('zislo');

// // // // // let message = (age < 14) ? 'z' :
// // // // //   (age < 90) ? 'b' :
// // // // //   (age >= 91) ? 'e' :
// // // // //   'Какой необычный возраст!';

// // // // // alert( message );
// // // // // outer: for (let i = 0; i < 3; i++) {

// // // // //     for (let j = 0; j < 3; j++) {
  
// // // // //       let input = prompt(`Значение на координатах (${i},${j})`, '');
  
// // // // //       // если пустая строка или Отмена, то выйти из обоих циклов
// // // // //       if (!input) break outer; // (*)
  
// // // // //       // сделать что-нибудь со значениями...
// // // // //     }
// // // // //   }
  
// // // // //   alert("iyhkbh ");
// // // // let i = 1;
// // // // while (i<3) {
// // // //     alert( `number ${i}!` );
// // // //     i++;
// // // //   }

// // // He:
// // // for (let v = 0;v<=100;) {
// // //     let v = prompt ("VVedite zislo");
// // //     if (!v) break;
// // //     // if (v<=100) continue;
// // //     alert("vvedeno verno");
// // // }
// // let number = +prompt('Введите число между 0 и 3', '');
// // switch(number){

// //     case '0':
// //         alert ("0");
// //         break;

// //     case '1':
// //         alert("1")
// //         break;

// //     case '2':  
// //     case '3':
// //         alert("2 or 3")  
// //     break;
// // }
// function chekAge(a,b){
//     if (a<b){
//         return (a);
//     } else {
//         return (b);
//     }
// };
// chekAge(4,8);