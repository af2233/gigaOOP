<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>


<style>
    section {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f5f5f5;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #333;
    }

    p {
        font-size: 16px;
        line-height: 1.6;
    }

    img {
        max-width: 100%;
        height: auto;
    }

    pre {
        background: #f4f4f4;
        padding: 10px;
        border: 1px solid #ddd;
        overflow-x: auto;
    }

    code {
        font-family: 'Courier New', Courier, monospace;
    }
</style>

<section>
    <div>
        {@html data.htmlContent}
    </div>
</section>