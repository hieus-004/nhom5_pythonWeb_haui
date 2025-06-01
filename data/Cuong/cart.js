
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    function addToCart(name, price, image) {
      const existing = cart.find(item => item.name === name);
      if (existing) {
        existing.quantity++;
      } else {
        cart.push({ name, price, image, quantity: 1 });
      }
      localStorage.setItem('cart', JSON.stringify(cart));
      alert("Đã thêm vào giỏ hàng!");
    }

    function showCart() {
      document.getElementById('search-section').classList.add('hidden');
      document.getElementById('cart-section').classList.remove('hidden');
      renderCart();
    }

    function backToSearch() {
      document.getElementById('search-section').classList.remove('hidden');
      document.getElementById('cart-section').classList.add('hidden');
      document.getElementById('success-section').classList.add('hidden');
    }

    function renderCart() {
  const body = document.getElementById('cart-body');
  const totalDisplay = document.getElementById('cart-total');
  body.innerHTML = '';
  let total = 0;

  cart.forEach((item, index) => {
    const itemTotal = item.price * item.quantity;
    total += itemTotal;
    body.innerHTML += `
       <tr>
    <td style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 12px;">
      <img src="${item.image}" style="width: 100px; border-radius: 8px;"/>
      <div style="text-align: center;">
        <div>${item.name}</div>
        <button onclick="removeItem(${index})" style="border: none; background: none; color:rgb(205, 200, 200); font-size: 20px; margin-top: 4px;">✖</button>
      </div>
    </td>
    <td>
      <button class="quantity-btn" onclick="changeQty(${index}, -1)">-</button>
      ${item.quantity}
      <button class="quantity-btn" onclick="changeQty(${index}, 1)">+</button>
    </td>
    <td style="color: #e66000; font-weight: bold;">${itemTotal.toLocaleString()}₫</td>
  </tr>
    `;
  });

  totalDisplay.innerText = total.toLocaleString() + '₫';
}


    function changeQty(index, delta) {
      cart[index].quantity += delta;
      if (cart[index].quantity < 1) cart[index].quantity = 1;
      localStorage.setItem('cart', JSON.stringify(cart));
      renderCart();
    }

    function removeItem(index) {
      cart.splice(index, 1);
      localStorage.setItem('cart', JSON.stringify(cart));
      renderCart();
    }

    function checkout() {
      if (cart.length === 0) {
        alert("Giỏ hàng trống!");
        return;
      }
      cart = [];
      localStorage.removeItem('cart');
      document.getElementById('cart-section').classList.add('hidden');
      document.getElementById('success-section').classList.remove('hidden');
    }
  