<script>
    /** @type {import('./$types').PageData} */
    export let data;
    console.log(data.par)
</script>


<style>
    section {
        width: 100%;
        height: 100%;
        background-color: #f5f5f5;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }
</style>

<section>
    <h1>{data.course} Course Page</h1>
</section>
