// paste this code in browser console and press enter

const calculateAverage = (marks) => {
  const sum = marks.reduce((acc, mark) => acc + mark, 0);
  return sum / marks.length;
};

const displayFibonacci = (n) => {
  let a = 0,
    b = 1,
    c;
  console.log(`Fibonacci series up to ${n} terms:`);
  for (let i = 1; i <= n; i++) {
    console.log(a);
    c = a + b;
    a = b;
    b = c;
  }
};

const isPalindrome = (str) => {
  const reversedStr = str.split("").reverse().join("");
  return str === reversedStr;
};

const menu = () => {
  let continueRunning = true;
  while (continueRunning) {
    const option = prompt(
      "Choose an option:\n1. Calculate Average\n2. Display Fibonacci Series\n3. Check Palindrome\n4. Exit"
    );
    switch (option) {
      case "1":
        const marksInput = prompt("Enter subject marks");
        const marksArray = marksInput.split(",").map(Number);
        const average = calculateAverage(marksArray);
        console.log(`Average Marks: ${average}`);
        break;
      case "2":
        const terms = parseInt(
          prompt("Enter the number of terms for Fibonacci series:"),
          10
        );
        displayFibonacci(terms);
        break;

      case "3":
        const str = prompt("Enter a string to check for palindrome:");
        const result = isPalindrome(str);
        console.log(`Is Palindrome: ${result}`);
        break;
      case "4":
        console.log("Exiting...");
        continueRunning = false;
        break;
      default:
        console.log("Invalid option. Please choose a valid option.");
        break;
    }
  }
};
menu();
