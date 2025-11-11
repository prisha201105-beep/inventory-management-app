import streamlit as st
from bst import BST

# Initialize BST
if "bst" not in st.session_state:
    st.session_state.bst = BST()

# --- Page Configuration ---
st.set_page_config(page_title="Inventory Management", page_icon="📦", layout="centered")

# --- Custom CSS for styling and floating icons ---
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f8cdda, #1d2b64);
    font-family: 'Poppins', sans-serif;
    color: white;
}

h1, h2, h3 {
    text-align: center;
    color: #ffffff;
}

div.stButton > button {
    background-color: #ff6b6b;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background-color: #f06595;
    transform: scale(1.05);
}

input, textarea {
    border-radius: 8px !important;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}

.icon {
    position: absolute;
    font-size: 30px;
    opacity: 0.2;
    animation: float 6s ease-in-out infinite;
}

.icon1 { left: 10%; top: 20%; animation-delay: 0s; }
.icon2 { left: 80%; top: 50%; animation-delay: 1s; }
.icon3 { left: 40%; top: 80%; animation-delay: 2s; }
.icon4 { left: 70%; top: 10%; animation-delay: 3s; }
</style>

<div class="icon icon1">📦</div>
<div class="icon icon2">💰</div>
<div class="icon icon3">🛒</div>
<div class="icon icon4">📊</div>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("📦 Inventory Management System")

# --- Tabs for different actions ---
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Item", "🔍 Search Item", "🗑️ Delete Item", "📋 View All"])

with tab1:
    st.subheader("Add New Item")
    item_id = st.number_input("Item ID", min_value=1)
    name = st.text_input("Item Name")
    price = st.number_input("Price", min_value=0.0)
    if st.button("Add Item"):
        st.session_state.bst.insert(item_id, name, price)
        st.success(f"✅ Item '{name}' added successfully!")

with tab2:
    st.subheader("Search Item by ID")
    search_id = st.number_input("Enter ID to Search", min_value=1, key="search")
    if st.button("Search"):
        result = st.session_state.bst.search(search_id)
        if result:
            st.info(f"📦 Item Found: **{result.name}** — 💰 Price: ₹{result.price}")
        else:
            st.error("❌ Item not found.")

with tab3:
    st.subheader("Delete Item")
    delete_id = st.number_input("Enter ID to Delete", min_value=1, key="delete")
    if st.button("Delete"):
        st.session_state.bst.delete(delete_id)
        st.warning(f"🗑️ Item with ID {delete_id} deleted (if it existed).")

with tab4:
    st.subheader("All Inventory Items")
    items = st.session_state.bst.inorder()
    if items:
        st.table(items)
    else:
        st.info("📭 No items available.")



