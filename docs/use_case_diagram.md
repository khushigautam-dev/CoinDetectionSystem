# Use Case Diagram

```mermaid
flowchart LR

    User((User))

    User --> A[Select Coin Image]
    User --> B[Run Coin Detection]
    User --> C[View Coin Count]
    User --> D[View Detection Result]
    User --> E[Save Result Image]

    B --> F[Preprocess Image]
    F --> G[Detect Coins]
    G --> H[Count Coins]
    H --> C
    G --> D
    D --> E