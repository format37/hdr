import cv2

def apply_hdr(image_path, blur_size=99, scale=256.0):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the BGR image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Split the image into its color channels
    r, g, b = cv2.split(img_rgb)

    # Apply the HDR effect to each color channel
    def hdr_channel(channel, blur_size, scale):
        # Apply Gaussian blur to the channel
        blurred = cv2.GaussianBlur(channel, (blur_size, blur_size), 0)
    
        # Invert the blurred channel
        inverted_blurred = 255 - blurred
    
        # Blend the original channel with the inverted blurred channel to create the HDR effect
        hdr = cv2.divide(channel, inverted_blurred, scale=scale)
    
        return hdr

    # Apply the HDR effect to each color channel
    hdr_r = hdr_channel(r, blur_size, scale)
    hdr_g = hdr_channel(g, blur_size, scale)
    hdr_b = hdr_channel(b, blur_size, scale)

    # Merge the HDR color channels back into a single image
    hdr_image = cv2.merge([hdr_r, hdr_g, hdr_b])

    return hdr_image

def main():
    hdr_image = apply_hdr('assets/in.png', blur_size=99, scale=215.0)
    cv2.imwrite('assets/out.png', hdr_image)

    # hdr_image = apply_hdr('assets/in.png', blur_size=49, scale=128.0)
    # Save the HDR image
    # cv2.imwrite('assets/out_49.png', hdr_image)

    # hdr_image = apply_hdr('assets/in.png', blur_size=199, scale=512.0)
    # Save the HDR image
    # cv2.imwrite('assets/out_199.png', hdr_image)


if __name__ == '__main__':
    main()
