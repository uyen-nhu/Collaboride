import qrcode
import replicate
import os
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import random

# Load our .env file to environment
load_dotenv()
# We got our access and secret key without hardcoding!
replicate_api_token = os.getenv('REPLICATE_API_TOKEN')


def make_qr_code_simple():
    qr = qrcode.QRCode(
            version=7,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
    )
    qr.add_data('https://www.freudenberg.com/')   # TODO: add a web link
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("assets/qr_code.png")

    return img


def make_qr_code_stylish():
    promts_collection = ['interior of luxury condominium with minimalist furniture and lush house plants and abstract wall paintings | modern architecture by makoto shinkai, ilya kuvshinov, lois van baarle, rossdraws and frank lloyd wright',
                         'The french countryside, green pastures, lush environment, vivid colors, animation by studio ghibli',
                         'a cubism painting of a town with a lot of houses in the snow with a sky background, Andreas Rocha, matte painting concept art, a detailed matte painting',
                         '1mechanical girl,ultra realistic details, portrait, global illumination, shadows, octane render, 8k, ultra sharp,intricate, ornaments detailed, cold colors, metal, egypician detail, highly intricate details, realistic light, trending on cgsociety, glowing eyes, facing camera, neon details, machanical limbs,blood vessels connected to tubes,mechanical vertebra attaching to back,mechanical cervial attaching to neck,sitting,wires and cables connecting to head',
                         'Japanese painting, mountains, 1girl',
                         'light, futobot, cyborg, ((masterpiece),(best quality),(ultra-detailed), (full body:1.2), 1male, solo, hood up, upper body, mask, 1boy, male focus,white gloves, cloak, long sleeves, spaceship, lightning, hires',
                         'A photo-realistic rendering of a busy market, ((street vendors, fruits, vegetable, shops)), (Photorealistic:1.3), (Highly detailed:1.2), (Natural light:1.2), art inspired by Architectural Digest, Vogue Living, and Elle Decor']
    output = replicate.run(
        "nateraw/qrcode-stable-diffusion:9cdabf8f8a991351960c7ce2105de2909514b40bd27ac202dba57935b07d29d4",
        input={
            "prompt": random.choice(promts_collection),
            "qr_code_content": 'https://www.freudenberg.com/',
            "negative_prompt": 'ugly, disfigured, low quality, blurry, nsfw',
            "num_inference_steps": 40,
            "guidance_scale": 7.5,
            "seed": 1234,
            "batch_size": 1,
            "strength": 0.9,
            "controlnet_conditioning_scale": 1.5}
    )

    # Download the image from the URL
    response = requests.get(output[0])
    response.raise_for_status()

    # Open the image using PIL
    image = Image.open(BytesIO(response.content))

    # Save the image to a file
    image.save('assets/qr_code.png')
