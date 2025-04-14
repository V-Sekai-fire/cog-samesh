# cog-samesh

A serverless deployment of the SAMesh model on Replicate.

## Overview

This repository contains the code necessary to deploy the SAMesh model as a serverless endpoint on Replicate. SAMesh is designed for 3D part segmentation workflows.

## 3D Part Segmentation Workflow

This workflow leverages [SAMesh](https://github.com/gtangg12/samesh) together with [HoloPart](https://vast-ai-research.github.io/HoloPart/). We picked SAMesh because it shares the MIT license with HoloPart, ensuring broad use in various projects.

Below is a concise comparison of SAMesh and its next-best alternative (SAMPart3D) for 3D part segmentation:

| Aspect                 | SAMesh [1][2]                                         | SAMPart3D [3][5]                                 |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------ |
| **Core Approach**      | Zero-shot 2D→3D lifting (SAM-based)                   | Trained MLPs on multiview renders                |
| **Input Requirements** | Untextured meshes                                     | Colored/textured meshes                          |
| **License**            | MIT [2]                                               | Not explicitly stated [6]                        |
| **Accuracy**           | Good generalization [1]                               | SOTA (72.1 mIoU on PartObjaverse) [5]            |
| **Compatibility**      | Broad support due to native mesh workflow             | Requires color data                              |
| **Strengths**          | - Fast setup<br>- Occlusion handling<br>- Lightweight | - Precise part boundaries<br>- Multi-granularity |
| **Weaknesses**         | - Surface-only segments<br>- Limited detail           | - Complex training pipeline<br>- GPU-heavy       |

**Why SAMesh + HoloPart is a Superior Combination:**

1. **License Safety**: Both use MIT licenses versus SAMPart3D’s unclear licensing.
2. **Pipeline Flexibility**: SAMesh segmentation followed by HoloPart amodal completion works seamlessly with untextured assets.
3. **Performance**: SAMesh’s 2D→3D lifting (around 50ms/frame [1]) suits real-time requirements much better than SAMPart3D’s MLP inference (~300ms [5]).

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
cog predict -i image=@/path/to/your/image.jpg
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
