"""Example application demonstrating structured logging patterns.

This module demonstrates:
- Hybrid dotted namespace logging pattern
- Request ID correlation
- Different log states (_started, _completed, _failed, etc.)
- Exception logging with stack traces
"""

import uuid

from app.core.logging import get_logger, set_request_id, setup_logging


def simulate_user_registration(email: str) -> dict[str, str]:
    """Simulate user registration with structured logging.

    Args:
        email: User email address

    Returns:
        User data dictionary
    """
    logger = get_logger()

    # Log registration started
    logger.info("user.registration_started", email=email, source="api")

    # Simulate validation
    logger.debug("user.email_validated", email=email, valid=True)

    # Simulate user creation
    user_id = str(uuid.uuid4())
    logger.info(
        "user.registration_completed",
        user_id=user_id,
        email=email,
        method="email_password",
    )

    return {"user_id": user_id, "email": email}


def simulate_database_operation() -> None:
    """Simulate database connection with structured logging."""
    logger = get_logger()

    logger.info("database.connection_started", host="localhost", port=5432)

    try:
        # Simulate successful connection
        logger.info(
            "database.connection_initialized",
            host="localhost",
            port=5432,
            pool_size=5,
        )
    except Exception as exc:
        logger.error(
            "database.connection_failed",
            host="localhost",
            port=5432,
            error=str(exc),
            exc_info=True,
        )
        raise


def simulate_api_request(user_id: str) -> dict[str, str]:
    """Simulate API request with request ID correlation.

    Args:
        user_id: User identifier

    Returns:
        Response data
    """
    logger = get_logger()

    # Set request ID for correlation
    request_id = str(uuid.uuid4())
    set_request_id(request_id)

    logger.info("api.request_started", method="GET", path="/users/me", user_id=user_id)

    # Simulate request processing
    response = {"user_id": user_id, "status": "active"}

    logger.info(
        "api.request_completed",
        method="GET",
        path="/users/me",
        status_code=200,
        duration_ms=42,
    )

    return response


def simulate_failed_operation() -> None:
    """Simulate a failed operation with error logging."""
    logger = get_logger()

    logger.info("payment.processing_started", amount=99.99, currency="USD")

    try:
        # Simulate payment failure
        raise ValueError("Insufficient funds")
    except Exception as exc:
        logger.error(
            "payment.processing_failed",
            amount=99.99,
            currency="USD",
            error=str(exc),
            exc_info=True,
        )


def main() -> None:
    """Run example demonstrations of structured logging."""
    # Setup logging
    setup_logging(log_level="DEBUG")

    logger = get_logger()
    logger.info("application.startup", environment="development", version="0.1.0")

    print("\n=== Example 1: User Registration ===")
    user = simulate_user_registration("user@example.com")
    print(f"Created user: {user}")

    print("\n=== Example 2: Database Connection ===")
    simulate_database_operation()

    print("\n=== Example 3: API Request with Request ID ===")
    response = simulate_api_request(user["user_id"])
    print(f"API response: {response}")

    print("\n=== Example 4: Failed Operation ===")
    simulate_failed_operation()

    logger.info("application.shutdown")


if __name__ == "__main__":
    main()
