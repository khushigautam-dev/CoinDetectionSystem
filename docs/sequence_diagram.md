# Sequence Diagram

```mermaid
sequenceDiagram

    actor User
    participant GUI
    participant ImageInput
    participant Processing
    participant Detector
    participant Counter
    participant Output

    User->>GUI: Select coin image
    GUI->>ImageInput: Load image
    ImageInput-->>GUI: Return image

    GUI->>Processing: Preprocess image
    Processing-->>GUI: Return processed image

    GUI->>Detector: Detect coins
    Detector-->>GUI: Return detected coins

    GUI->>Counter: Count coins
    Counter-->>GUI: Return total count

    GUI->>Output: Save result image
    Output-->>GUI: Confirm result saved

    GUI-->>User: Display coin count and result