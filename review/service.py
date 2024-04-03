import streamlit as st
from review.repository import ReviewRepository


class ReviewService:

    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie, stars, comment):
        review = dict(
            filme=movie,
            stars=stars,
            comentario=comment
        )
        new_review = self.review_repository.create_review(review)  # Retorno da api tá sendo status_code == 200. O certo é 201.
        st.session_state.reviews.append(new_review)
        return new_review
