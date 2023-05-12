// Load the LTM API library
const ltm = require('./ltm');

// Connect to the LTM server
const token = await ltm.connect();
console.log(`Connected to LTM server with token: ${token}`);

// Retrieve the contents of the user's memory
const memory = await ltm.getMemory();
console.log(`User's memory:`, memory);

// Add an item to the user's memory
await ltm.addMemory({ item: 'Example item' });
console.log('Item added to user\'s memory');

// Remove an item from the user's memory by ID
await ltm.removeMemory(12345);
console.log('Item removed from user\'s memory');

// Clear all items from the user's memory
await ltm.clearMemory();
console.log('All items cleared from user\'s memory');

// Display a notification to the user
ltm.notifyUser('Hello!');
console.log('Notification displayed');
