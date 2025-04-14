# cog-samesh

A serverless deployment of the SAMesh model on Replicate.

## Overview

This repository contains the code necessary to deploy the SAMesh model as a serverless endpoint on Replicate. SAMesh is designed for 3D part segmentation workflows.

## 3D Part Segmentation Workflow

This workflow leverages [SAMesh](https://github.com/gtangg12/samesh) together with [HoloPart](https://vast-ai-research.github.io/HoloPart/). We picked SAMesh because it shares the MIT license with HoloPart, ensuring broad use in various projects.

Below is a comparison of the benefits of SAMesh and SAMPart3D for 3D part segmentation:

| Aspect                 | SAMesh                                                 | SAMPart3D                                                          |
| ---------------------- | ------------------------------------------------------ | ------------------------------------------------------------------ |
| **Core Approach**      | Zero-shot 2D→3D lifting (SAM-based)                    | Trained MLPs on multiview renders                                  |
| **Input Requirements** | Works seamlessly with untextured meshes                | Optimized for colored/textured meshes                              |
| **License**            | MIT                                                    | Not explicitly stated                                              |
| **Accuracy**           | Generalizes well across various scenarios              | Achieves SOTA (72.1 mIoU on PartObjaverse)                         |
| **Compatibility**      | Supports native mesh workflows                         | Leverages color data for enhanced segmentation                     |
| **Strengths**          | - Quick setup<br>- Handles occlusions<br>- Lightweight | - Delivers precise part boundaries<br>- Supports multi-granularity |

**Why SAMesh + HoloPart is a Powerful Combination:**

1. **License Alignment**: Both use MIT licenses, ensuring compatibility and safety for diverse projects.
2. **Workflow Synergy**: SAMesh segmentation combined with HoloPart amodal completion provides a robust pipeline for untextured assets.
3. **Efficiency**: SAMesh’s 2D→3D lifting (around 50ms/frame [1]) is well-suited for real-time applications, complementing HoloPart’s capabilities.

**Example Use Case**:  
_Vehicle Customization Tool_  
SAMesh quickly segments visible parts (such as wheels and doors), then HoloPart infers complete geometries. This allows downstream processes to apply physics and textures to the completed parts.

## How to Use with API

Learn more about the available API endpoints from the [Replicate API Documentation](https://replicate.com/hardikdava/rf-detr/api).

## Local Development and Testing

To test the model locally before deployment:

```bash
# Install cog if you haven't already
pip install cog

# Run a prediction with a local image
cog predict -i mesh_file=@thirdparty/jacket.glb
```

## How to Use Custom Models

Customizing the deployment with your own model weights is simple:

1. Add your model weights file to the root of this repository.
2. Update the model initialization in [predict.py](predict.py). For example:

   ```python
   # Change this line in predict.py
   self.model = models.get("samesh", checkpoint_path="your-custom-model.pth")
   ```

3. Follow the [Replicate deployment guide](https://replicate.com/docs/guides/deploy-a-custom-model) to publish your model.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/V-Sekai-fire/cog-samesh/blob/main/LICENSE) file for details.
