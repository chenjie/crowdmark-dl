from PIL import ImageDraw, ImageFont
import os


def savePDF(cma, im_list, course_dir):
    print()
    if not im_list:
        return
    out_pdf_filename = os.path.join(course_dir, cma.assessment_name)
    im_list[0].save(out_pdf_filename + ".pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list[1:])

def drawFrontPageText(cma, pil_img, font):
    cursor_pos = 0
    ImageDraw.Draw(pil_img).text((30, 0), 
        'Title: {}'.format(cma.assessment_name), (0, 0, 128), font=font)
    ImageDraw.Draw(pil_img).text((30, 30), 
        'Course Name: {}'.format(cma.course_name), (0, 0, 128), font=font)
    ImageDraw.Draw(pil_img).text((30, 60), 
        'Instructor: {}'.format(cma.instructor.name), (0, 0, 128), font=font)
    ImageDraw.Draw(pil_img).text((30, 90), 
        'Instructor Email: {}'.format(cma.instructor.email), (0, 0, 128), font=font)
    ImageDraw.Draw(pil_img).text((30, 120), 
        'Date: {}'.format(cma.mark_sent_out_date.to('local').format(
            'YYYY-MM-DD dddd HH:mm:ss ZZZ')), (0, 0, 128), font=font)
    if cma.points == 0:
        ImageDraw.Draw(pil_img).text((30, 150), 'Not graded.', (255, 0, 0), font=font)
    else:
        ImageDraw.Draw(pil_img).text((30, 150), 
            'Total Score: {}% ({}/{})'.format(int(cma.points/cma.total_points * 100), 
            cma.points, cma.total_points), (165, 42, 42), font=font)
    cursor_pos += 180
    return pil_img, cursor_pos

def drawTextBasedOnPageList(cma, pil_img, page_list, question, cursor_pos, font):
    if not any(page_list):
        if question.points is None:
            ImageDraw.Draw(pil_img).text((30, cursor_pos), 'Not graded.', (255, 0, 0), font=font)
        else:
            ImageDraw.Draw(pil_img).text((30, cursor_pos), 
                'Score: {}/{}'.format(question.points, question.total_points
                ), (255, 0, 0), font=font)
    else:
        ImageDraw.Draw(pil_img).text((30, cursor_pos), 'Cont.', (255, 0, 0), font=font)
    return pil_img

def adjustFontSize(pil_img, img_fraction=0.4):
    txt = 'Instructor Email: hello.world@mail.utoronto.ca'
    fontsize = 1
    font = ImageFont.truetype("google-fonts/OpenSans-Regular.ttf", fontsize)
    while font.getsize(txt)[0] < img_fraction*pil_img.size[0]:
        fontsize += 1
        font = ImageFont.truetype("google-fonts/OpenSans-Regular.ttf", fontsize)
    return font