from django.shortcuts import render
from datetime import date

text = '''<p>Accusantium consectetur a explicabo vero numquam dolorum totam accusamus unde, sint impedit ea culpa aperiam nemo, totam ducimus corrupti omnis quaerat tenetur quos dolorum ut. Officia fuga ullam dolorem, vel itaque est tenetur mollitia iusto excepturi culpa soluta in quisquam labore, impedit necessitatibus architecto rerum magni commodi, eius dignissimos illo repellendus iste aliquid minus obcaecati dolor, reiciendis omnis fugiat quos odio quibusdam.</p>

<p>Neque eveniet ab assumenda repellendus molestias voluptatibus aperiam earum, qui beatae possimus similique magni enim mollitia tenetur, voluptatum facilis natus earum ad repudiandae a tempora quam hic cupiditate molestiae? Error non iure nemo ipsum quaerat id obcaecati animi quidem a, similique laborum rem est officia nulla molestiae illo, consequuntur beatae odio ab ullam illo molestiae voluptates harum inventore soluta similique. Minima sint blanditiis temporibus, quas optio voluptatem earum tenetur aperiam sint accusantium enim cum pariatur, harum atque exercitationem quidem dolores officiis qui non impedit quam, officia similique quibusdam consectetur ea nostrum?</p>

<p>Quisquam in laudantium recusandae aliquam magni sapiente consectetur tempore, tenetur nulla nam odit odio vel animi ipsam enim, accusamus fugiat quis facere dicta voluptate voluptatem aut optio dolor, nisi corrupti delectus? Nemo reiciendis in aperiam est adipisci iusto unde, vero praesentium veniam aspernatur doloribus, earum enim et vero tenetur recusandae pariatur repellendus asperiores, ducimus accusamus consectetur et nemo fugiat harum id praesentium perspiciatis porro?</p>

<p>Delectus corporis optio, harum aut quam dolorem tenetur, omnis debitis excepturi vero iste quod? Architecto recusandae consequatur obcaecati neque accusamus magni expedita temporibus quidem vitae nobis?</p>

<p>Natus iusto exercitationem veniam accusamus libero consequuntur aut, ratione rerum suscipit ipsum minus? Repellendus ea odit maiores labore eum earum, cum possimus a voluptatibus odio tempora, corporis tempora quidem assumenda aut doloremque earum nisi maxime quam nihil, quia explicabo labore vel blanditiis tenetur laboriosam sed ad, dignissimos facilis aperiam consequatur.</p>

<p>Neque odit quam saepe magni amet libero officiis sapiente omnis, tempore ab quas fuga atque quam cumque nam aut.</p>

<p>Voluptatum earum nisi quaerat at maxime animi ex dolor esse unde, pariatur beatae explicabo quis itaque ut earum voluptates natus veniam, ex illo itaque. Quibusdam nulla asperiores blanditiis soluta magnam nisi eum, delectus expedita placeat? Vero facilis inventore veniam ea, explicabo sit dolores iste, quam adipisci facere alias unde nobis blanditiis nesciunt atque velit, quas numquam id, nobis autem exercitationem sunt tempora officia odio fugit assumenda tempore nihil.</p>

<p>Iusto voluptate distinctio totam, laboriosam aperiam vel ducimus ipsum molestiae officia nihil, architecto voluptatibus delectus ducimus, corrupti esse officia consequatur, sequi sit tempore doloremque excepturi debitis consequuntur culpa temporibus quaerat reiciendis?</p>

<p>Officia officiis blanditiis aliquid natus id assumenda dignissimos, iste itaque illum, expedita alias tempora iure doloremque facilis? Consequatur voluptatibus provident aut sapiente aliquam voluptatum ducimus saepe ad praesentium atque, commodi quas amet eos quidem voluptate eaque facere.</p>
'''



# Create your views here.
all_posts = [
    {
        "slug": "Django",
        "image": "django.jpg",
        "author": "Matheus Eduardo",
        "date": date(2024, 9, 26),
        "title": "Aprendendo Django",
        "excerpt": "Lorem ipsum dolor sit amet. Eum incidunt nisi quo alias corrupti At quaerat consequuntur aut natus consequatur et totam blanditiis quo corrupti laborum.",
        "content": text
    },
    {
        "slug": "Sass",
        "image": "sass.png",
        "author": "Matheus Eduardo",
        "date": date(2024, 9, 26),
        "title": "Aprendendo Sass",
        "excerpt": "Lorem ipsum dolor sit amet. Eum incidunt nisi quo alias corrupti At quaerat consequuntur aut natus consequatur et totam blanditiis quo corrupti laborum.",
        "content": text
    },
    {
        "slug": "React-Native",
        "image": "react-native.png",
        "author": "Matheus Eduardo",
        "date": date(2024, 9, 26),
        "title": "Aprendendo React Native",
        "excerpt": "Lorem ipsum dolor sit amet. Eum incidunt nisi quo alias corrupti At quaerat consequuntur aut natus consequatur et totam blanditiis quo corrupti laborum.",
        "content": text
    }
    
]

# Função temporária
def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latests_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latests_posts
    })

def posts(request):
    return render(request, "blog/posts.html", {"all_posts": all_posts})

def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": post})