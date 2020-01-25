import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ImageToByteArray {

    public static void main(String args[]){
        int imageOption = 0;
        int colorOption = 0;

        if (args.length > 0 && !args[0].isEmpty()) {
            imageOption = Integer.parseInt(args[0]);
        }
        if (args.length > 1 && !args[1].isEmpty()) {
            colorOption = Integer.parseInt(args[1]);
        }

        String[] imagefiles = new String[]{"bridge1.jpg", "bridge2.jpg", "bridge3.jpg"};
        try {

            BufferedImage bufferedImage = ImageIO.read(new File(imagefiles[imageOption%3]));
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
            ImageIO.write(bufferedImage, "jpg", byteArrayOutputStream);
            byte[] bytes = byteArrayOutputStream.toByteArray();

            ByteArrayInputStream bis = new ByteArrayInputStream(bytes);
            BufferedImage bufferedImage2 = ImageIO.read(bis);

            int width = bufferedImage2.getWidth();
            int height = bufferedImage2.getHeight();

            if (colorOption!=0) {
                for (int y = 0; y < height; y++) {
                    for (int x = 0; x < width; x++) {
                        int p = bufferedImage2.getRGB(x, y);
                        int a = (p >> 24) & 0xff;

                        switch (colorOption) {
                            case 1:
                                //red
                                int red = (p >> 16) & 0xff;
                                p = (a << 24) | (red << 16) | (0 << 8) | 0;
                                break;
                            case 2:
                                //green
                                int green = (p >> 8) & 0xff;
                                p = (a << 24) | (0 << 16) | (green << 8) | 0;
                                break;
                            case 3:
                                //blue
                                int blue = p & 0xff;
                                p = (a << 24) | (0 << 16) | (0 << 8) | blue;
                                break;
                            default:
                                int random = p & 0xf0;
                                p = (a << 24) | (0 << 16) | (0 << 6) | random;
                                break;

                        }
                        bufferedImage2.setRGB(x, y, p);
                    }
                }
            }
            ImageIO.write(bufferedImage2, "jpg", new File("output.jpg"));

        } catch (IOException e) {
            System.out.println(e);
        }


    }
}