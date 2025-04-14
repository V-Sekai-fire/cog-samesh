from cog import BasePredictor, BaseModel, Path
import trimesh
from omegaconf import OmegaConf
from samesh.data.loaders import *
from samesh.models.sam_mesh import *


class ModelOutput(BaseModel):
    segmented_mesh: Path

class Predictor(BasePredictor):
    def setup(self):
        pass

    def predict(self, mesh_file: Path) -> ModelOutput:
        """
        Run SAMesh segmentation on the input mesh.
        
        Args:
            mesh_file (Path): Path to the input mesh file in GLB format.
        
        Returns:
            ModelOutput: Contains the path to the segmented mesh in GLB format.
        """
        config = OmegaConf.load('../configs/mesh_segmentation.yaml')
        segmented_mesh = segment_mesh(mesh_file, config, visualize=False)
        output_path = self.output_path("segmented_mesh.glb")
        segmented_mesh.export(output_path)
        return ModelOutput(segmented_mesh=output_path)
