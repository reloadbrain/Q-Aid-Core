from pytorchxai.xai.cam_gradcam import GradCam
from pytorchxai.xai.cam_scorecam import ScoreCam
from pytorchxai.xai.gradient_guided_backprop import GuidedBackprop
from pytorchxai.xai.gradient_guided_gradcam import GuidedGradCam
from pytorchxai.xai.gradient_integrated_grad import IntegratedGradients
from pytorchxai.xai.gradient_smooth_grad import SmoothGrad
from pytorchxai.xai.gradient_vanilla_backprop import VanillaBackprop


class GradientVisualization:
    def __init__(self, model):
        self.model = model

        self.visualizations = [
            GuidedBackprop(model),
            VanillaBackprop(model),
            ScoreCam(model),
            GradCam(model),
            GuidedGradCam(model),
            IntegratedGradients(model),
            SmoothGrad(model),
        ]

    def generate(self, orig_image, input_image, target):
        results = {}
        for v in self.visualizations:
            results.update(v.generate(orig_image, input_image, target))
        return results
