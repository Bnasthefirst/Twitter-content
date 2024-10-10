// Check if MetaMask is installed
async function checkMetaMask() {
  if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
    return true;
  } else {
    alert('MetaMask is not installed. Please install MetaMask to use this feature.');
    return false;
  }
}

// Connect to MetaMask wallet
async function connectWallet() {
  try {
    if (await checkMetaMask()) {
      // Request wallet connection
      const accounts = await ethereum.request({ method: 'eth_requestAccounts' });

      // Display the connected account
      const walletAddress = accounts[0];
      document.getElementById('walletAddress').innerText = `Connected Wallet: ${walletAddress}`;
      console.log('Connected to MetaMask:', walletAddress);
    }
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
  }
}

// Attach the function to the button click
document.getElementById('connectWalletButton').addEventListener('click', connectWallet);
