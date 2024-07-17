$(document).ready(function() {
    // Función para manejar la acción de "Agregar al carrito"
    $('.agregar-carrito').click(function(e) {
        e.preventDefault();
        var productoId = $(this).data('id');
        $.ajax({
            url: "/agregar/" + productoId + "/",
            type: 'GET',
            success: function(data) {
                $('#mensaje').text(data.message).fadeIn().delay(2000).fadeOut();
            }
        });
    });

    // Función para manejar la acción de "Ver" pero por el momento no se usa
    $('.ver-producto').click(function() {
        var cardBody = $(this).closest('.card').find('.card-body');
        cardBody.toggleClass('expanded');
    });
});
