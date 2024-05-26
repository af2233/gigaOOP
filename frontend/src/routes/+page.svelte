<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>


<style type="text/scss">
	section{
		width: 100%;
		height: 100%;
		background-color: #f5f5f5;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.content{
        max-width: 1024px;
        width: 100%;
        margin-top: 80px;   
        padding: 0 15px;
    }

    .heading{
        font-size: 40px;
        font-weight: 600;
        margin-bottom: 50px;
    }

    .courses{
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    .courses__item{
        background-color: #FFDE4B;
        padding: 15px;
        max-width: 600px;
        width: 100%;
        max-height: 150px;
        height: 150px;
        transition: .2s;
        &:hover{
            filter: brightness(110%);
        }
    }

    .courses__title{
        font-size: 36px;
        font-weight: 600;
    }
</style>

<section>
    <div class="content">
        <h1 class="heading">Курсы</h1>
        <div class="courses">
            {#each data.courses as course}
                <a href={`/${course.id}?title=${encodeURIComponent(course.title)}`} class="courses__item">
                    <h2 class="courses__title">{course.title}</h2>
                </a>
            {/each}
        </div>
    </div>
</section>

