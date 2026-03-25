# Virtualization

- `SfRichTextBoxAdv` supports UI virtualization: the control creates UI elements only for the document content currently visible in the viewer. 

- Elements for content that becomes visible while scrolling are created on demand. 

- Virtualization reduces memory usage and improves UI scrolling and rendering performance for large documents.


## What virtualization does

- Creates visual elements only for visible content (pages/lines/blocks) rather than the entire document model.

- Lowers memory footprint and reduces layout cost when working with large documents.

- UI elements are generated lazily as the user scrolls or navigates.


## How to use

- Virtualization is enabled by the control's internal behavior; the control virtualizes UI by default to optimize performance.