# Class Diagram

```mermaid
classDiagram

class ImageInput {
    +load_image(path)
}

class ImagePreprocessing {
    +convert_to_grayscale(image)
    +apply_threshold(image)
}

class CoinDetector {
    +find_contours(image)
    +detect_coins(contours)
}

class CoinCounter {
    +count_coins(image_path)
}

class ResultDisplay {
    +display_result(image_path, count)
}

class GUI {
    +select_image()
    +run_detection()
    +show_result()
}

ImageInput --> ImagePreprocessing
ImagePreprocessing --> CoinDetector
CoinDetector --> CoinCounter
CoinCounter --> ResultDisplay
GUI --> ImageInput
GUI --> CoinCounter
GUI --> ResultDisplay