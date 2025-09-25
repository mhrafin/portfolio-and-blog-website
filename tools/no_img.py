from bs4 import BeautifulSoup
from typing import Optional


def no_img(html: Optional[str]) -> str:
    if not html:
        return html or ""

    soup = BeautifulSoup(html, "html.parser")
    

    for img in soup.find_all("img"):
        img.decompose()

    return str(soup)

# no_img(
#     html="""
# <div class="rounded-lg p-4 md:p-8 md:m-8 mb-8 bg-eerie-black">
#     <div class="flex flex-col md:flex-row gap-8 md:gap-12">
#       <div class="md:flex-1 rounded-[18px] overflow-hidden ">
#         <!-- outer inset border for the image area -->

#         <!-- inner rounded panel (like the inner rounded corner in the sketch) -->
        
#           <img class="w-full max-h-100 aspect-auto object-cover object-center transform-gpu transition-transform duration-300 ease-out scale-[1.06] hover:scale-[1.00] origin-center motion-reduce:transition-none motion-reduce:transform-none" src="/images/me.jpg" alt="">
        
#       </div>
#       <div class="md:flex-1 flex flex-col justify-between">
#         <div>
#           <h1 class="text-4xl md:text-5xl font-extrabold tracking-wide mb-6">
#             Hey It's me, Raf!
#           </h1>

#           <div class="space-y-3">
#             <div class="flex items-center gap-4">
#               <section class="font-medium"><p>Hi, My name is Raf, And I am here to talk about myself. Not much to say. Good Bye. See you Monday.</p>
# <p><img alt="Two guys" src="../images/its_me_raf-1758447911794.jpeg">
# Fig: Two human talking to each other</p></section>
#             </div>
#           </div>
#         </div>

#         <div class="mt-6 flex justify-end">
#           <a href="/blog/hey-its-me-raf.html">
#             <button class="px-5 py-2 rounded-xl border-1 border-persian-red hover:border-sea-green text-lg font-medium shadow-sm hover:bg-sea-green transition" type="button">
#               Read More
#             </button>
#           </a>
#         </div>
#       </div>
#     </div>
#   </div>
# """
# )
