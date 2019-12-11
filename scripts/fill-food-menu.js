  
// function randomString() {
//     return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
// }

let orderArray = [];

const populateFood = async function() {
    // console.dir(menuFile);
    $.getJSON("scripts/menu-items.json", function(menuData) {
        
        console.dir(menuData);
        const foodMenuElement = document.getElementById("food-menu"); 
        console.dir(foodMenuElement);
        
        menuData.menu.forEach(category => {
           
            categorySection = document.createElement("section"); 
            categoryHeading = document.createElement("h3");
            categoryHeading.innerText = category.name; 
            categorySection.appendChild(categoryHeading); 
            foodMenuElement.appendChild(categorySection); 
            let categorySize = 0;
            category.items.forEach(item => {
              
                itemName = document.createElement("h4"); 
                itemName.innerText = item.name; 
                categorySection.appendChild(itemName); 
                itemDesc = document.createElement("p");
                itemDesc.innerText = item.description;
                categorySection.appendChild(itemDesc);
                itemPrice = document.createElement("b");
                itemPrice.innerText = '$' + item.price;
                categorySection.appendChild(itemPrice);
               
                button = document.createElement("button");
                button.innerText = "Add to Online Order";
                button.onclick = function() {
                    orderArray.push(item);
                    updateCart(orderArray);
                }
                categorySection.appendChild(button);
             
                if (item.image) {
                    itemImage = document.createElement("img");
                    itemImage.setAttribute("src", item.image);
                    
                    categorySection.appendChild(itemImage);
                    categorySize++;
                }
                categorySize++;
                console.log(categorySize + category.name);
                categorySection.setAttribute("style", "grid-row: span " + categorySize);
            });
        });
    });
}