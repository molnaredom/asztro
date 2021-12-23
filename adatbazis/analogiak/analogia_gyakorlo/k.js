
// const request = async () => {
//     const response = await fetch('../package.json');
//     const json = await response.json();
//     return json
// }
//
// let k =request();
// console.log(k)


// const data = await (await fetch('../package.json')).json();
//
// console.log(data);


async function getUserAsync()
{
  let response = await fetch(`../package.json`);
  let data = await response.json()
  return data;
}

getUserAsync().then(data => console.log(data));
let data = getUserAsync().then(data => console.log(data));

console.log("1",data)
console.log("2", data["version"])


