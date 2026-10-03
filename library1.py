import streamlit as st

# ─────────────────────────────────────────────────────────────
# PAGE SETUP
# ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Library Management",
    page_icon="📚",
    layout="wide"
)

st.title("📚 The Bombay Bound — Library Management System")
st.caption("Library Services of India | Dictionary + Streamlit Demo Project")
st.divider()


# ─────────────────────────────────────────────────────────────
# BOOK DATABASE
# ─────────────────────────────────────────────────────────────

BOOKS = {
    "B001": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Classic",
        "description": "A witty classic about love, family, first impressions, and social expectations.",
        "interest": "Romance, classics",
        "allotment": 1,
        "alloted_member": "Abhinav Sinha",
        "member_id": "M001",
        "contact": "abhi@yahoo.com",
        "issue_date": "28/09/2026",
        "returned": False,
        "image_url": "https://cdn2.penguin.com.au/covers/original/9780141330167.jpg",
    },

    "B002": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "description": "A portrait of ambition, wealth, and the American dream in the Jazz Age.",
        "interest": "Classics, society",
        "allotment": 1,
        "alloted_member": "Nisha das",
        "member_id": "M002",
        "contact": "nisha@gmail.com",
        "issue_date": "25/06/2026",
        "returned": False,
        "image_url": "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781982146702/the-great-gatsby-9781982146702_hr.jpg",
    },

    "B003": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "description": "A coming-of-age story exploring justice, empathy, and community.",
        "interest": "Justice, classics",
        "allotment": 0,
        "alloted_member": "",
        "member_id": "",
        "contact": "",
        "issue_date": "",
        "returned": True,
        "image_url": "https://cdn2.penguin.com.au/covers/original/9781785151552.jpg",
    }
}


# ─────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────

if "selected_book" not in st.session_state:
    st.session_state.selected_book = "B001"

if "book_alloted" not in st.session_state:
    st.session_state.book_alloted = False


# ─────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────

tab1, tab2 = st.tabs([
    "🔍 Discover & Search Books",
    "🧾 Issued Books & Members"
])


# ═════════════════════════════════════════════════════════════
# TAB 1 — SEARCH / DISCOVER BOOKS
# ═════════════════════════════════════════════════════════════

with tab1:

    st.subheader("🔍 Find a book that fits your mood")

    # Get all authors
    authors = []

    for book_id in BOOKS:
        authors.append(BOOKS[book_id]["author"])

    # Author selection
    book_aut = st.selectbox(
        "Select BOOK author:",
        options=sorted(authors)
    )

    # Find selected book
    selected_id = None

    for book_id in BOOKS:
        if BOOKS[book_id]["author"] == book_aut:
            selected_id = book_id
            break

    if selected_id:
        st.session_state.selected_book = selected_id

    book = BOOKS[st.session_state.selected_book]

    st.divider()

    # ─────────────────────────────────────────────────────────
    # BOOK CARD
    # ─────────────────────────────────────────────────────────

    col_photo, col_info = st.columns([1, 3])

    with col_photo:
        st.image(
            book["image_url"],
            width=220
        )

    with col_info:

        st.markdown(f"## 📖 {book['title']}")

        st.markdown(
            f"**Author:** {book['author']}  \n"
            f"**Genre:** {book['genre']}  \n"
            f"**Description:** {book['description']}  \n"
            f"**Interest:** {book['interest']}"
        )

        st.divider()

        if book["allotment"] == 0:

            st.success("🟢 Available for issue")

        else:

            st.warning(
                f"🔴 Currently allotted to {book['alloted_member']}"
            )


# ═════════════════════════════════════════════════════════════
# TAB 2 — ISSUE BOOKS & ALLOTMENTS
# ═════════════════════════════════════════════════════════════

with tab2:

    st.subheader("🧾 Issuing Books")

    book_id = st.session_state.selected_book
    book = BOOKS[book_id]

    # ─────────────────────────────────────────────────────────
    # CURRENT BOOK
    # ─────────────────────────────────────────────────────────

    st.markdown(f"### 📚 {book['title']}")

    if book["allotment"] == 0:

        st.success("🟢 This book is currently available.")

        st.divider()

        st.markdown("### 👤 Member Details")

        member_name = st.text_input(
            "Enter member name:",
            placeholder="Example: Amit"
        )

        member_id = st.text_input(
            "Enter member ID:",
            placeholder="Example: M003"
        )

        contact = st.text_input(
            "Enter contact:",
            placeholder="Example: amit@gmail.com"
        )

        # Issue button
        if st.button(
            "📚 Issue Book",
            use_container_width=True
        ):

            if member_name and member_id:

                book["alloted_member"] = member_name
                book["member_id"] = member_id
                book["contact"] = contact
                book["allotment"] = 1
                book["returned"] = False
                book["issue_date"] = "30/09/2026"

                st.session_state.book_alloted = True

                # ─────────────────────────────────────────
                # SCREEN EFFECT
                # ─────────────────────────────────────────

                st.balloons()

                st.success(
                    f"🎉 Book successfully allotted to {member_name}!"
                )

                st.markdown(
                    f"""
                    <div style="
                        padding: 20px;
                        border-radius: 15px;
                        background-color: #E8F5E9;
                        border: 2px solid #4CAF50;
                        text-align: center;
                        margin-top: 15px;
                    ">
                        <h2>📚 Book Allotted Successfully!</h2>
                        <p><b>Book:</b> {book['title']}</p>
                        <p><b>Member:</b> {member_name}</p>
                        <p><b>Member ID:</b> {member_id}</p>
                        <p><b>Status:</b> 🟢 Issued</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.error(
                    "⚠️ Please enter both Member Name and Member ID."
                )

    else:

        # ─────────────────────────────────────────────────────
        # BOOK ALREADY ISSUED
        # ─────────────────────────────────────────────────────

        st.error("🔴 This book is currently not available.")

        st.markdown(
            f"""
            <div style="
                padding: 20px;
                border-radius: 15px;
                background-color: #FFF3E0;
                border: 2px solid #FF9800;
            ">
                <h3>📕 Current Allotment Details</h3>
                <p><b>Book:</b> {book['title']}</p>
                <p><b>Allotted To:</b> {book['alloted_member']}</p>
                <p><b>Member ID:</b> {book['member_id']}</p>
                <p><b>Contact:</b> {book['contact']}</p>
                <p><b>Issue Date:</b> {book['issue_date']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ─────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────

st.divider()

st.caption(
    "📚 The Bombay Bound | Library Management System | "
    "Streamlit Demo Project"
)
