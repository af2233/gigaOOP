<script>
    /** @type {import('./$types').PageData} */
    import Quiz from '$lib/Quiz.svelte';
    export let data;
</script>


<style>
    .content{
        max-width: 730px;
        margin: 0 auto;
        width: 100%;
        margin-top: 80px;   
        padding: 0 25px;
    }

    .heading{
        font-size: 40px;
        font-weight: 600;
        margin-bottom: 50px;
    }

    .chapter-content{
        max-width: 100%;
        object-fit: contain;

        & img{
            object-fit: contain;
            display: block;
            width: 100%;
            margin: 0 auto;
            max-width: 100%;
        }

        & h1, h2, h3, h4, h5, h6{
            margin-top: 40px;
            font-size: 24px;
            line-height: 1.25;
            font-weight: 700;
        }

        & p{
            font-size: 18px;
            line-height: 1.6;
            margin-top: 30px;
        }

        & pre {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            padding: 15px;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
        }
        & code {
            color: #333;
        }
    }

    
</style>

<section>
    <div class="content">
        <h1 class="heading">{data.themeTitle}</h1>
        <div class="chapter-content">{@html data.htmlContent}</div>
        <Quiz title={data.quizData.title} questions={data.quizData.questions} />
    </div>
</section>
