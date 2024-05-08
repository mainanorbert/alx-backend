const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];


const getItemById =(id)=>{
  return listProducts.find((product)=>product.id === id)
}




import redis from 'redis';
import {promisify} from 'util'

const client = redis.createClient()
const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)

const reserveStockById =(itemId, stock)=>{
    client.set(`item.${itemId}`, stock)
};

const getCurrentReservedStockById = async(itemId) =>{
  const reservedStock = await getAsync(`item.${itemId}`)
  return reservedStock? parseInt(reservedStock): 0;
}

const express = require('express')
const app = express()
const port = 1245

app.get('/list_products', (req, res) => {
    const availableItems = listProducts.map((product)=>({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    }))
    res.json(availableItems)
}
)

app.get('/list_products/:itemId', async(req, res)=>{
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId)
   
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const reservedStock = await getCurrentReservedStockById(itemId)
    const availableStock = product.stock - reservedStock;
    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: availableStock
    })
})

app.get('/reserve_product/:itemId', async(req, res) =>{
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId)
   
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const reservedStock = await getCurrentReservedStockById(itemId)
    const availableStock = product.stock - reservedStock
    if (availableStock <= 0){
        return res.json({ status: 'Not enough stock available', itemId: product.id });
    }
    reserveStockById(itemId, reservedStock + 1);
    return res.json({"status":"Reservation confirmed","itemId":1})

})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))