// steps:

// npm i fs
// node Server.js
// choose write function first

const fs = require("fs");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function showMenu() {
  console.log("\nChoose an operation:");
  console.log("1. Read");
  console.log("2. Access");
  console.log("3. Open");
  console.log("4. Write");
  console.log("5. Append");
  rl.question(
    "\nEnter the number corresponding to the operation: ",
    handleUserChoice
  );
}

function handleUserChoice(choice) {
  const filePath = "./exxp.txt";

  switch (choice) {
    case "1":
      fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
          console.error("Error reading file:", err);
        } else {
          console.log("File content:\n", data);
        }
        rl.close();
      });
      break;

    case "2":
      fs.access(filePath, fs.constants.F_OK, (err) => {
        if (err) {
          console.error("File does not exist:", err);
        } else {
          console.log("File is accessible.");
        }
        rl.close();
      });
      break;

    case "3":
      fs.open(filePath, "r", (err, fd) => {
        if (err) {
          console.error("Error opening file:", err);
        } else {
          console.log("File opened successfully. File descriptor:", fd);
        }
        rl.close();
      });
      break;

    case "4":
      rl.question("Enter the text to write to the file: ", (text) => {
        fs.writeFile(filePath, text, "utf8", (err) => {
          if (err) {
            console.error("Error writing to file:", err);
          } else {
            console.log("File written successfully.");
          }
          rl.close();
        });
      });
      break;

    case "5":
      rl.question("Enter the text to append to the file: ", (text) => {
        fs.appendFile(filePath, text, "utf8", (err) => {
          if (err) {
            console.error("Error appending to file:", err);
          } else {
            console.log("Text appended successfully.");
          }
          rl.close();
        });
      });
      break;
    default:
      console.log("Invalid choice, please choose a valid operation.");
      showMenu();
  }
}

showMenu();
