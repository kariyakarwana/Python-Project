from fastapi import FastAPI
from app.routes import accounts, auth, transactions

app = FastAPI(
    title="Banking API",
    description="API for managing accounts and transactions.",
    version="1.0.0"
)

app.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])