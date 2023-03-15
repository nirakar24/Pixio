# How it works ?

## Kernel blurring (using filter2D() )
- Make a kernel 
- Apply the kernel using filter2D().

```python
kernel = np.ones((shape), npfloat32)/dimension #normalizing
output_kernel = cv2.filter2D(img_path, depth, kernel)
cv.imshow("blurred_img", output_kernel)
```
## Water Color Art
- Input image and resize it : <br>
This step ensures proper kernel applications for Images with different dimensions.

- Clear the impurities : <br>
1.Median Blur <br>
2.Edge preserving blur <br><br>
The impurities may be colour variations due to which filters may lag.

- Apply filter : <br>
Create the effect that is desired on the image by applying bilateral filter (it reduces the noise in the image)

- Tune the art : <br>
Tuning may include sharpening, dehazing, contrast enhancement, etc.
In this algoritm we sharpenend the image by creating a gaussian mask and subtracting it from the original image.

<div>
<img width="400" alt="main2" src="https://user-images.githubusercontent.com/101456316/225216832-6839eb31-8f86-4798-bd8c-e62281ae1eea.jpg">
<img width="400" alt="main2" src="https://user-images.githubusercontent.com/101456316/225216868-8071c8f1-d1f4-443d-9955-c4cf04f3bf8b.png"></div>




