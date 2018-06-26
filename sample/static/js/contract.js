
 var userAccount;
 window.addEventListener('load', function() {
   // Checking if Web3 has been injected by the browser (Mist/MetaMask)
    if (typeof web3 !== 'undefined') {
      // Use Mist/MetaMask's provider
      web3js = new Web3(web3.currentProvider);
      var propertyAddress = "0x6bce6808e453eec53fbf5a727a6ce48276ef06ab";
      propertyContract = new web3js.eth.Contract(property_ABI, propertyAddress);
      console.log("Contract created");
    } else {
      console.log("No provider present");
    }
});


function isPropertyOwned(id) {
    return propertyContract.methods.isPropertyOwned(id).call()
}

function buyProperty(name, latitude, longitude, venueId) {
    $("#status").attr("disabled", "disabled");
    $("#status").html("Transction in progress");
    return propertyContract.methods.buyProperty(name, latitude, longitude, venueId)
    .send({from: web3.eth.defaultAccount})
    .on("receipt", function(receipt) {
      console.log("Added property")
      console.log(receipt);
      $("#status").html('Property owned');
      $("#status").attr("disabled", "disabled");
    })
    .on("error", function(error) {
      console.log("Inside  Error")
      console.log(error);
      $("#status").attr("disabled", false);
      $("#status").html('Buy');
    });
}