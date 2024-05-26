<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>


<style>
    .content{
        max-width: 1024px;
        margin: 0 auto;
        width: 100%;
        margin-top: 80px;   
        padding: 0 15px;
    }

    .heading{
        font-size: 40px;
        font-weight: 600;
        margin-bottom: 50px;
    }

    .chapters__title{
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    .chapters__list{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .chapters__item{
        border: 1px solid #0a0a0a;
        padding: 30px;
        transition: .3s;
        &:hover{
            color: #fff;
            background-color: #0a0a0a;
        }
    }

    .chapters__text{
        font-size: 20px;
        font-weight: 600;
    }
</style>

<section>
    <div class="content">
        <h1 class="heading">Course Page</h1>
        <div class="chapters">
            <h2 class="chapters__title">Главы</h2>
            <div class="chapters__list">
                {#each data.themes as theme}
                    <a href={`/${data.courseId}/${theme.id}`} class="chapters__item">
                        <p class="chapters__text">{theme.title}</p>
                    </a>
                {/each}
            </div>
        </div>
    </div>
</section>
