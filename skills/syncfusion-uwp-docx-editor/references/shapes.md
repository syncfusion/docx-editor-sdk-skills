# Shapes in UWP DOCX Editor

Shape support in the Syncfusion UWP DOCX Editor allows viewing and interacting with shapes that exist in imported documents.

## Supported Shapes
The editor preserves the following shape types when opening documents:
- Text boxes
- Rectangles

> Note: The editor does not provide APIs to insert new shapes at runtime. Only shapes already present in imported documents are supported.

## Shape Interaction
The editor allows limited interaction with preserved shapes:
- Shapes can be resized using built-in resize handles (mouse or touch).
- Shape position and layout are preserved when documents are loaded.
- Shapes with **Inline with Text** wrapping can be dragged within the document.

## Supported Wrapping Styles
The editor preserves these wrapping styles for images and text box shapes:
- Inline with Text  
- Behind Text  
- In Front of Text  
- Top and Bottom  
- Square  

## Text wrapping style preservation
- At present, only **shape preservation** with the above text-wrapping styles is supported.

- **Modifying existing shapes** (such as changing wrapping styles) is **not supported**.

> Note:
> - **Behind Text** and **In Front of Text** are supported starting from version **18.3.0.x**.
> - **Top and Bottom** is supported starting from version **19.1.0.x**.
> - **Tight** and **Through** wrapping styles are displayed as **Square** in the editor.