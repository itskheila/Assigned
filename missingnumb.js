//Given a list containing n distinct numbers 
//from 0 to n, find the missing number.
//Input: [3, 0, 1]
//Output: 2
//NOTE: No number limit


function missingNumber(numbs) {
  for (let number = 0; number <= numbs.length; number++) 
    // theres a list of numbers 3 0 1
    // let number = 0 works for the first loop
    // the loop for numbers will go through each number
    //it checks through numbs.length, confirming yes this exsists
  
    {
    if (!numbs.includes(number)) 
// this if statement checks if the number is not in the numbs array, 
// it returns that number
        {
      return number;
    }
  }
}


console.log(missingNumber([3, 0, 1])); 
