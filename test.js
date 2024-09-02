// Custom Error Class
class CustomError extends Error {
  constructor(message) {
      super(message);
      this.name = this.constructor.name;
  }
}

const readlineSync = require('readline-sync');

// Function to demonstrate division with error handling
function divisionOperation(a, b) {
  try {
      if (b === 0) {
          throw new Error('Division by zero is not allowed.');
      }
      if (typeof a !== 'number' || typeof b !== 'number') {
          throw new TypeError('Both arguments must be numbers.');
      }
      return a / b;
  } catch (error) {
      console.error(`Operation failed: ${error.message}`);
      return null;
  } finally {
      console.log('Division operation attempt completed.');
  }
}

// Function to handle user input with retry logic
function getNumberInput(promptMessage) {
  let result;
  while (true) {
      result = Number(readlineSync.question(promptMessage));
      if (isNaN(result)) {
          console.log('Please enter a valid number.');
      } else {
          return result;
      }
  }
}

// File System Operations (Node.js example)
const fs = require('fs').promises;

async function fileOperation() {
  try {
      await fs.readFile('non_existent.txt', 'utf8');
  } catch (error) {
      if (error.code === 'ENOENT') {
          console.log('File does not exist. Would you like to create it?');
          const answer = readlineSync.question('Enter Y to create, N to cancel: ').toLowerCase();
          if (answer === 'y') {
              await fs.writeFile('non_existent.txt', 'This file was created due to an ENOENT error.');
              console.log('File has been created.');
          } else {
              console.log('File creation cancelled.');
          }
      } else {
          console.error('An error occurred:', error.message);
      }
  }
}

// Menu system for demonstration
function menu() {
  console.log("\nError Handling Demonstrations in JavaScript:");
  console.log("1. Division Operation");
  console.log("2. Age Validation");
  console.log("3. File Operation (requires Node.js)");
  console.log("4. Exit");
  return readlineSync.question("Choose an option (1-4): ");
}

// Age validation with custom error
function validateAge(age) {
  if (age < 0 || age > 120) {
      throw new CustomError('Age must be between 0 and 120.');
  }
  console.log(`Age ${age} is valid.`);
}

// Main function to run the menu
async function main() {
  while (true) {
      let choice = menu();
      switch (choice) {
          case '1':
              let dividend = getNumberInput('Enter dividend: ');
              let divisor = getNumberInput('Enter divisor: ');
              let result = divisionOperation(dividend, divisor);
              if (result !== null) console.log(`Result: ${result}`);
              break;
          case '2':
              try {
                  let age = getNumberInput('Enter your age: ');
                  validateAge(age);
              } catch (e) {
                  if (e instanceof CustomError) {
                      console.log(e.message);
                  } else {
                      console.log('Unexpected error:', e.message);
                  }
              }
              break;
          case '3':
              await fileOperation();
              break;
          case '4':
              console.log('Exiting the program. Goodbye!');
              return;
          default:
              console.log('Invalid option. Please try again.');
      }
  }
}

// Run the main function
main().catch(e => console.error('An unexpected error occurred:', e));
